# Use Python 3.10.10 as the base image
FROM python:3.10.10

# Set the working directory
WORKDIR /app

# Copy the required files into the container
COPY requirements.txt .
COPY discord_bot.py .

# Install the required packages
RUN pip install -r requirements.txt

# Run your Discord.py application inside the container
CMD [ "python", "discord_bot.py" ]