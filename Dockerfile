# Use Python 3.10.10 as the base image
FROM python:3.10.10

# Set the working directory
WORKDIR /app

# Check if discord_bot.py exists and update the repository if necessary
RUN pip install -r requirements.txt

# Run your Discord.py application inside the container
CMD [ "python", "discord_bot.py" ]