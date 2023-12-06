package main

import (
	"database/sql"
	"fmt"
	"html/template"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

type Film struct {
	Name  string `json:"name"`
	Plot  string `json:"plot"`
	Photo string `json:"photo"`
}

func home_page(w http.ResponseWriter, r *http.Request) {
	http.Handle("/images/film/", http.StripPrefix("/images/film/", http.FileServer(http.Dir("./images/film"))))
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

	var Films []Film
	for dbfilms.Next() {
		var film Film
		err = dbfilms.Scan(&film.Name, &film.Plot, &film.Photo)
		if err != nil {
			panic(err)
		}
		Films = append(Films, film)
	}

	tmp.ExecuteTemplate(w, "home_page", Films)
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

func handleFunc() {
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static/"))))
	http.HandleFunc("/", home_page)
	http.HandleFunc("/new_review/", new_review_page)
	http.HandleFunc("/autor_page/", autor_page)
	http.ListenAndServe("localhost:8000", nil)
}

func main() {
	handleFunc()
}
