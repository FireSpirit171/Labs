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

/*
var film1 = Film{
	"Interstellar",
	"When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
	"images/film/Interstellar.jpg"}

var film2 = Film{
	"The Martian",
	"During a manned mission to Mars, astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded on the hostile planet. With limited supplies, he must find a way to signal Earth that he is alive.",
	"images/film/TheMartian.jpg",
}

var film3 = Film{
	"Gravity",
	"Dr. Ryan Stone, a medical engineer, and astronaut Matt Kowalski find themselves adrift in space after their shuttle is destroyed. With no communication to Earth and limited oxygen, they must work together to survive and find a way back home.",
	"images/film/Gravity.jpg",
}

var film4 = Film{
	"Arrival",
	"When mysterious spacecraft touch down across the globe, an elite team, led by linguist Louise Banks, is brought together to decipher their intent. As tensions rise between nations, Banks races against time to understand the aliens language to prevent a global war.",
	"images/film/Arrival.jpg",
}

var film5 = Film{
	"The Matrix",
	"Thomas Anderson, a computer programmer, discovers the truth about his reality - it is a simulated world created by sentient machines to subdue human minds. With the help of rebels, he fights to free humanity from the control of the machines.",
	"images/film/TheMatrix.jpg",
}

var Films = []Film{film1, film2, film3, film4, film5}*/

func home_page(w http.ResponseWriter, r *http.Request) {
	http.Handle("/images/film/", http.StripPrefix("/images/film/", http.FileServer(http.Dir("./images/film"))))
	tmp, _ := template.ParseFiles("templates/home_page.html")
	tmp.Execute(w, w) //Здесь нужно заменит второй w
}

func autor_page(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "The autor of this website")
}

func handleRequest() {
	http.HandleFunc("/", home_page)
	http.HandleFunc("/autor/", autor_page)
	http.ListenAndServe("localhost:8000", nil)
}

func main() {
	//handleRequest()

	db, err := sql.Open("mysql", "root:root@tcp(127.0.0.1:3306)/film_reviews")
	if err != nil {
		panic(err)
	}

	defer db.Close()

	/* Новый фильм
	insert, err := db.Query("INSERT INTO films (name, plot, photo) VALUES ('Arrival', 'When mysterious spacecraft touch down across the globe, an elite team, led by linguist Louise Banks, is brought together to decipher their intent. As tensions rise between nations, Banks races against time to understand the aliens language to prevent a global war.', 'images/film/Arrival.jpg')")
	if err != nil {
		panic(err)
	}
	insert.Close()*/

	//Получение фильмов
	res, err := db.Query("SELECT name, plot, photo FROM films")
	if err != nil {
		panic(err)
	}

	for res.Next() {
		var film Film
		err = res.Scan(&film.Name, &film.Plot, &film.Photo)
		if err != nil {
			panic(err)
		}

		fmt.Println(fmt.Sprintf("Name: %s\nPlot: %s\nPhoto: %s", film.Name, film.Plot, film.Photo))
	}
}
