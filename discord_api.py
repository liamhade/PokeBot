from typing import List, Dict
import requests
import json

def get_channel_messages(channel_id: int, headers_file: str) -> List[Dict]:
	"""Grabs last 50 Discord messages from a specific channel."""
	with open(headers_file, "r") as f:
		headers = json.load(f)

	url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50"
	resp = requests.get(url, headers=headers)
	
	return resp.json()

if __name__ == "__main__":
	headers_file = "static/discord_headers.json"
	channel_id = "802706129753735188" # Channel with Kat

	messages = get_channel_messages(channel_id, headers_file)