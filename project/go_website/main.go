package main

import (
	"fmt"
	"html/template"
	"net/http"
)

type Film struct {
	name  string
	plot  string
	photo string
}

func home_page(w http.ResponseWriter, r *http.Request) {
	film1 := Film{"Interstellar", "When Earth becomes uninhabitable in the future," +
		"a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft," +
		"along with a team of researchers, to find a new planet for humans.",
		"https://m.media-amazon.com/images/I/A1JVqNMI7UL._AC_UF1000,1000_QL80_.jpg"}
	tmp, _ := template.ParseFiles("templates/home_page.html")
	tmp.Execute(w, film1)
}

func autor_page(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "The autor of this website")
}

func handleRequest() {
	http.HandleFunc("/", home_page)
	http.HandleFunc("/autor/", autor_page)
	http.ListenAndServe(":8000", nil)
}

func main() {
	handleRequest()
}
