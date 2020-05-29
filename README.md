# weed-data-bw
This is the data engineering side of the project

# Views:
When you visit these urls, you can access the following info

## GET [/](https://weed-data-bw.herokuapp.com/)


# APIs:
Base URL is https://weed-data-bw.herokuapp.com

## POST [/model](https://weed-data-bw.herokuapp.com/model)

### Request:
JSON object in the following format:

```js
{
    "Flavors": ["Blueberry", "Apple", "Skunk"],
    "Effects": ["Focused", "Happy", "Relaxed"]
}
```
It has to have 2 keys "Flavors" and "Effects" in it. Each of their values are an array which contain at most 3 strings.

### Response:
JSON: list of dictionaries, each with 4 keys:</br>
{
    "Name" -> string,
    "Description" -> string,
    "Flavors" -> list of 3 strings,
    "Effects" -> list of 3 strings
]
```js
[
    {
        "Name": "Agent Tangie",
        "Description": "Agent Tangie is a ...",
        "Flavors": [
            "Cirtus",
            "Diesel",
            "Earthy"
        ],
        "Effects": [
            "Energetic",
            "Focused",
            "Giggly"
        ]
    },
    {
        "Name":...,
        ...
    },
    ...
]
```
<hr>

## GET [/strains](https://weed-data-bw.herokuapp.com/strains)

### Request:
Request's body is empty

### Response:
JSON: list of a dictionaries which each contain 59 keys ("name", "description", <57 one-hot-encoded features>) there also is an endpoint for a not one-hot-encoded version ([/web_layout_strains](https://weed-data-bw.herokuapp.com/web_layout_strains)):</br>
```js
[
    {
        "name": "24K Gold",
        "description": "24K Gold, also known as...",
        "Ammonia": 0,
        "Apple": 0,
        "Apricot": 0,
        "Berry": 1,
        "Blue Cheese": 0,
        <'other 52 one-hot-encoded features'>
    },
    {
        "name": ...,
        ...
    },
    ...
]
```

<hr>

## GET [/web_layout_strains](https://weed-data-bw.herokuapp.com/web_layout_strains)

### Request:
Request's body is empty

### Response:
JSON: list of a dictionaries which each contain 4 keys ("name", "description", "flavors", "effects") there also is an endpoint for a one-hot-encoded version ([/strains](https://weed-data-bw.herokuapp.com/strains)):</br>
```js
[
    {
        "name": "24K Gold",
        "description": "24K Gold, also known as...",
        "flavors": [
            "Blueberry",
            "Mango",
            "Spicy/Herbal"
        ],
        "effects": [
            "Creative",
            "Giggly",
            "Relaxed"
        ]
    },
    {
        "name": ...,
        ...
    },
    ...
]