package main

import (
	"fmt"
	"net/http"
)

func home_page(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello website")
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
