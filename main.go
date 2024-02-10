package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/games", GetGames)
	router.Run("localhost:8080")
}

type Games struct {
	Username      string
	MostValueGame string
	GamesOwned    int
}

func GetGames(c *gin.Context) {
	testResponse := Games{"Jason", "TF2", 42}

	c.IndentedJSON(http.StatusOK, testResponse)

}
