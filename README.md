# PokeBot

## Creation Notes

First, it's always good to create a virtual environment. You don't want things to get too messy.

Second, let's get some version control going so we don't lose track of any changes.

I was having some issues with getting the FastAPI setup. This was my original function:

```
app.get("/")
def read_root():
	return {"message": "Hello world!"}
```

It took me a long time to realize that there was a missing "@" symbol. Adding it back in gave me this:

```
@app.get("/")
def read_root():
	return {"message": "Hello world!"}
```

The lesson here is simple: pay attention to the details. If the functions look okay, dig deeper, until you're looking at individual characters.


