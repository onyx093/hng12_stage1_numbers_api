# Number Classification API

## Description

A simple FastAPI-based public API that takes a number value and return some interesting mathematical properties and fun facts about that number.

## Endpoint

**GET** [https://hng12-stage1-number-classification-api-rho.vercel.app/api/classify-number?number=37](https://hng12-stage1-number-classification-api-rho.vercel.app/api/classify-number?number=37)

### Response Example (200 OK)

```json
{
  "number": 37,
  "is_prime": true,
  "is_perfect": false,
  "digit_sum": 10,
  "properties": ["odd"],
  "fun_fact": "37 is the cost in cents of the Whopper Sandwich when Burger King first introduced it in 1957."
}
```

### Response Example (400 Bad Request)

```json
{
  "number": "\"37\"",
  "error": true
}
```

## Setup Instructions

1. Clone the repo:

```
git clone https://github.com/onyx093/hng12_stage1_numbers_api
cd hng12_stage1_numbers_api
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the API locally:

```
uvicorn main:app --reload
```

### Hiring Links

[Hire Python Developers](https://hng.tech/hire/python-developers)
[Hire C# Developers](https://hng.tech/hire/csharp-developers)
[Hire Golang Developers](https://hng.tech/hire/golang-developers)
[Hire PHP Developers](https://hng.tech/hire/php-developers)
[Hire Java Developers](https://hng.tech/hire/java-developers)
[Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)
