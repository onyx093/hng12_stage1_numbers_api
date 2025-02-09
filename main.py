from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import math

app = FastAPI()


def is_prime(n: int) -> bool:
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_perfect(n: int) -> bool:
    """
    A perfect number is a positive integer that is equal to the sum
    of its proper divisors (excluding itself). For example, 6 is perfect
    because 1 + 2 + 3 = 6.
    """
    if n <= 1:
        return False
    total = 1  # 1 is always a proper divisor (for n > 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n


def is_armstrong(n: int) -> bool:
    """
    An Armstrong (or Narcissistic) number is one that is the sum of its own digits
    each raised to the power of the number of digits.
    Example: 371 → 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371.
    """
    if n < 0:
        return False  # Typically defined for non-negative numbers only.
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n


def digit_sum(n: int) -> int:
    """Compute the sum of the digits of the absolute value of n."""
    return sum(int(d) for d in str(abs(n)))

@app.get("/")
def root():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to the Number Classifier API!",
        "built_by": "Olaleye Obidiya(Onyx_Oceanview)",
        "github_repo": "https://github.com/onyx093/hng12_stage1_numbers_api",
    }

@app.get("/api/classify-number")
def classify_number(number: str):
    """
    GET endpoint to classify a number.
    Query Parameter:
      - number: the integer to classify.
    
    Success (200 OK) Response JSON:
      {
          "number": 371,
          "is_prime": false,
          "is_perfect": false,
          "properties": ["armstrong", "odd"],
          "digit_sum": 11,
          "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
      }
    
    Error (400 Bad Request) Response JSON:
      {
          "number": "alphabet",
          "error": true
      }
    """
    try:
        num = int(number)
    except ValueError:
        # Return 400 Bad Request if the provided number cannot be converted to an integer.
        return JSONResponse(status_code=400, content={"number": number, "error": True})

    # Compute basic mathematical properties.
    result = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "digit_sum": digit_sum(num),
    }

    # Collect interesting properties.
    properties = []
    if num >= 0 and is_armstrong(num):
        properties.append("armstrong")
    if num > 0 and is_perfect(num):
        properties.append("perfect")
    # Determine parity.
    properties.append("even" if num % 2 == 0 else "odd")
    result["properties"] = properties

    # Retrieve a fun fact from the Numbers API.
    try:
        fun_fact_response = requests.get(f"http://numbersapi.com/{num}?json")
        if fun_fact_response.status_code == 200:
            data = fun_fact_response.json()
            result["fun_fact"] = data.get("text", "")
        else:
            result["fun_fact"] = ""
    except Exception:
        result["fun_fact"] = ""

    return result
