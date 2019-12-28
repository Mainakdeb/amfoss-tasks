use std::io;
extern crate regex;
use regex::Regex;


fn main() {
    let mut input = String::new();
    println!("enter email id boi:");
    match io::stdin().read_line(&mut input) {
        Ok(_) => {       
            //here
            let email_regex = Regex::new(r"^([a-z0-9_+]([a-z0-9_+.]*[a-z0-9_+])?)@([a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,6})").unwrap();
            //email addresses are not case sensitive
            let email_addresses = [input];
            for email_address in &email_addresses {
                println!("Valid email id?: {} ", email_regex.is_match(email_address))
            }
        }
        Err(e) => println!("oppsie : {}", e)
    }
}