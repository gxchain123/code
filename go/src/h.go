package main

import "fmt"
import "time"

// This program will print "Hello from main goroutine".
// It MIGHT print "Hello from another goroutine".
func main() {
  go fmt.Println("Hello from another goroutine")
  fmt.Println("Hello from main goroutine")

  // At this point the program execution stops and all
  // active goroutines are killed.
  time.Sleep(time.Second)
}
