package main

import "fmt"

type Person struct {
	name    string
	surname string
	age     int
}

func main() {
	emp1 := Person{"Bob", "Neverback", 25}
	fmt.Println("1)", emp1.info())
}

func (emp *Person) info() string {
	var info string = emp.name + " " + emp.surname + " " + fmt.Sprint(emp.age)
	return info
}
