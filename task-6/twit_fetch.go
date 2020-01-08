package main

import (

	"log"
	"flag"
	"fmt"
	"os"
	"bufio" //for str input
	"strings"

	"github.com/coreos/pkg/flagutil"
	"github.com/dghubble/go-twitter/twitter"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/clientcredentials"
)

func main() {
	flags := struct {
		consumerKey    string
		consumerSecret string
	}{}

	flag.StringVar(&flags.consumerKey, "consumer-key", "Your_consumer_key", "Twitter Consumer Key")
	flag.StringVar(&flags.consumerSecret, "consumer-secret", "Your_consumer_secret", "Twitter Consumer Secret")
	flag.Parse()
	flagutil.SetFlagsFromEnv(flag.CommandLine, "TWITTER")

	if flags.consumerKey == "" || flags.consumerSecret == "" {
		log.Fatal("Access Token required")
	}

	config := &clientcredentials.Config{
		ClientID:     flags.consumerKey,
		ClientSecret: flags.consumerSecret,
		TokenURL:     "https://api.twitter.com/oauth2/token",
	}
	httpClient := config.Client(oauth2.NoContext)

	// Twitter client
	client := twitter.NewClient(httpClient)


	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter a Twitter Username: ")
	user_name_bro, _ := reader.ReadString('\n')

	params := &twitter.UserShowParams{ScreenName: user_name_bro}
	user, resp, err := client.Users.Show(params)
	_ = resp
	_ = err
	
	strbro := fmt.Sprintf("%#v", user)
	final_index := strings.Index(strbro,"Notifications")
	final_index1 := final_index -2

	strboi := strbro[40:final_index1]

	//skidaddle

	f, err := os.Create(user_name_bro+"_Twitter_data.txt")
    if err != nil {
        fmt.Println(err)
        return
    }
    l, err := f.WriteString(strboi)
    if err != nil {
        fmt.Println(err)
        f.Close()
        return
    }
	fmt.Println(l, "bytes written successfully")
	fmt.Println("The text file has been saved :)")
    err = f.Close()
    if err != nil {
        fmt.Println(err)
		return
	}
	
}


