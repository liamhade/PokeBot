# PokeBot

## USAGE

The `headers.json` file has two fields, `Authorization` and `Cookie` that need to be fetched from browser during an actual request.

## CREATION NOTES

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

I think I need to rethink how to get notified when a Target restocks. Since I'm not the manager of the Discord server, I can't add a bot to those servers.

Another issue that I'm coming up against is that I don't know what exactly I'm looking for. What Pokemon cards should I be buying? There's a Discord server that has that information, so we just need to channel the Discord information into my Python application. 

I'm trying to create a Python script that sniffs the packets in a Discord server, so I can be notified when a specific message arises.