const fetch = require("node-fetch");
const userList = [
    {
        blogs: 0,
        rating: 1
    },
    {
        blogs: 1,
        rating: 1
    },
    {
        blogs: 0,
        rating: 3
    },
    {
        blogs: 12,
        rating: 13
    },
    {
        blogs: 1,
        rating: 21
    },
    {
        blogs:10,
        rating: 32
    },
    {
        blogs: 32,
        rating: 21
    },
    {
        blogs: 0,
        rating: 54
    },
    {
        blogs: 32,
        rating: 2
    },
    {
        blogs: 0,
        rating: 34
    },
    {
        blogs: 1,
        rating: 21
    },
    {
        blogs:10,
        rating: 32
    },
    {
        blogs: 32,
        rating: 21
    },
    {
        blogs: 0,
        rating: 54
    },
    {
        blogs: 32,
        rating: 2
    },
    {
        blogs: 0,
        rating: 34
    },
]

const newList = userList.filter((blog, index) => index < 10);

// console.log('newList = ', newList)
// console.log('newList.length = ', newList.length)


const ratingsLength = newList.length
const listRatings = [];
for (let i = 0; i < ratingsLength; i++) {
    listRatings.push(newList[i].rating);
}
console.log('listRating = ', listRatings);
// arra.sort((a,b)  => a-b )
// console.log(arra)

async function* asyncGenerator() {
    let i = 0;
    while (i < 1) {
        yield i++;
    }
}

(async function() {
    for await (let num of asyncGenerator()) {
        const username = `user${num}`
        let response = await fetch("http://127.0.0.1:8000/admin/users/customuser/add/", {
            "credentials": "include",
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,ru-RU;q=0.8,ru;q=0.5,en;q=0.3",
                "Content-Type": "application/x-www-form-urlencoded",
                "Upgrade-Insecure-Requests": "1"
            },
            "referrer": "http://127.0.0.1:8000/admin/users/customuser/add/",
            "body": `csrfmiddlewaretoken=kFANf6vbK0uMXXYxP25RyR6ZSOhGkpr2DjwlrvQ4Bj3dgIIUdKZR9kCpxAEWOeIY&username=${username}&password1=969vW4EhGeVQd7J&password2=969vW4EhGeVQd7J&_addanother=Save+and+add+another`,
            "method": "POST",
            "mode": "cors"
        });
        let text = await response.text()
        console.log(text);
    }
})();
