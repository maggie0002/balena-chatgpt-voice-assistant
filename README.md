# A WIP ChatGPT voice assistant running on a Raspberry pi.

TODO:

- Implement https://github.com/vvanglro/cf-clearance for handling Cloudflare authorisation
- Integration with Balena as per: https://github.com/maggie0002/picovoice-balena-cli
- Add ability to cancel while running
- Modify the ChatGPT Python module to accept user_agent headers in \_chatgpt_headers, session token and cf_token like chatgpt/api.py

Notes:

Required packages

pvporcupine \
pvrecorder \
pvcheetah \
gtts
revChatGPT
