package main

import (
	"database/sql"
	"fmt"
	"html/template"
	"io"
	"net/http"
	"os"
	"strings"

	_ "github.com/go-sql-driver/mysql"
)

type Film struct {
	Name  string `json:"name"`
	Plot  string `json:"plot"`
	Photo string `json:"photo"`
}

func home_page(w http.ResponseWriter, r *http.Request) {
	mux := http.NewServeMux()
	tmp, err := template.ParseFiles("templates/home_page.html")
	if err != nil {
		panic(err)
	}

	db, err := sql.Open("mysql", "root:root@tcp(127.0.0.1:3306)/film_reviews")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	dbfilms, err := db.Query("SELECT name, plot, photo FROM films")
	if err != nil {
		panic(err)
	}

	Films := []Film{}
	for dbfilms.Next() {
		var film Film
		err = dbfilms.Scan(&film.Name, &film.Plot, &film.Photo)
		if err != nil {
			panic(err)
		}
		Films = append(Films, film)
	}

	tmp.ExecuteTemplate(w, "home_page", Films)
	http.ListenAndServe("localhost:8000", mux)
}

func new_review_page(w http.ResponseWriter, r *http.Request) {
	tmp, err := template.ParseFiles("templates/new_review.html")
	if err != nil {
		panic(err)
	}

	tmp.ExecuteTemplate(w, "new_review", nil)
}

func autor_page(w http.ResponseWriter, r *http.Request) {
	fmt.Println("The autor of this website")
}

func save_new_review(w http.ResponseWriter, r *http.Request) {

	r.ParseMultipartForm(10 << 20)
	name := r.FormValue("filmName")
	plot := r.FormValue("plot")
	file, _, err := r.FormFile("posterLink")

	cname := strings.ReplaceAll(name, " ", "") //Убираем из названия пробелы
	//Далее обработка полученного в поле постер файла
	if err != nil {
		panic(err)
	}
	defer file.Close()

	//Создаем новый файл в папке для сохранения
	newFile, err := os.Create("./images/film/" + cname + ".jpg")
	if err != nil {
		panic(err)
	}

	//Копируем содержимое первого файла в новый файл
	io.Copy(newFile, file)

	//Далее добавляем в БД запись
	db, err := sql.Open("mysql", "root:root@tcp(127.0.0.1:3306)/film_reviews")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	insert, err := db.Query(fmt.Sprintf("INSERT INTO films (name, plot, photo) VALUES ('%s', '%s', '%s')", name, plot, "images/film/"+cname+".jpg"))
	if err != nil {
		panic(err)
	}
	defer insert.Close()

	http.Redirect(w, r, "/", http.StatusSeeOther)
}

func handleFunc() {
	http.Handle("/images/film/", http.StripPrefix("/images/film/", http.FileServer(http.Dir("./images/film"))))
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static/"))))
	http.HandleFunc("/", home_page)
	http.HandleFunc("/new_review/", new_review_page)
	http.HandleFunc("/save_new_review/", save_new_review)
	http.HandleFunc("/autor_page/", autor_page)
	http.ListenAndServe("localhost:8000", nil)
}

func main() {
	handleFunc()
}
