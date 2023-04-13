# Tigerify v0.4
Music app for sharing music, little test to learn the use of Angular and Flask. Now v0.4 includes an user system with basic login functionalities.

## Introduction
Tigerify is developed in Python, using the framework Flask, and Angular, and is a music streaming platform that allows users to listen to music on-demand. The platform has a wide variety of songs and music genres, which users can access through a set of endpoints for GET, POST, PUT, and DELETE requests. 

This wikia page will provide an overview of the app's features, architecture, and endpoints.

## Features
Tigerify is developed with Flask and Angular, and has the following features:

User authentication: Users can create accounts and log in to the platform using their email and password.
Music streaming: Users can search for and stream music on-demand, using the app's search functionality and music player.
Music genres: The app supports a wide variety of music genres, including rock, pop, hip-hop, classical, and more.
Song management: Users can manage their music library by adding, removing, and editing songs.
Endpoint support: The app provides a set of endpoints for GET, POST, PUT, and DELETE requests, which can be used to retrieve, add, update, and delete songs and music genres.

Tigerify is a mock project that utilizes Flask, a popular web framework written in Python, to create a Spotify-like application. Here is a brief overview of how Flask is used in Tigerify:

- Routing: Flask allows you to map different URLs (routes) to specific functions in your Python code. In Tigerify, you can define routes such as /login and /search to handle different user actions.
- Templates: Flask uses Jinja2 as its template engine, which allows you to create dynamic HTML pages by inserting variables and logic into your HTML templates. Tigerify uses templates to display search results, user profiles, and playlists.
- Forms: Flask provides a built-in way to handle user input through forms. In Tigerify, users can log in and search for songs using HTML forms that submit data to the Flask app.
- Models: Flask does not come with an ORM (Object-Relational Mapping) like Django, but it is easy to integrate third-party ORMs such as SQLAlchemy. In Tigerify, SQLAlchemy is used to define database models for users, songs, playlists, and other entities.
- Authentication: Flask provides a way to handle user authentication and session management through its Flask-Login extension. In Tigerify, Flask-Login is used to manage user sessions and restrict access to certain routes.

## Architecture
Tigerify uses a three-tier architecture, consisting of the following layers:

Presentation layer: This layer is responsible for handling user interface interactions, such as displaying the music player and search functionality.
Business logic layer: This layer contains the business logic of the app, such as handling user authentication, music streaming, and song management.
Data access layer: This layer is responsible for accessing and manipulating data in the app's database, which stores information about songs and music genres.

## Endpoints
The Tigerify app developed in Python and Angular provides the following endpoints for GET, POST, PUT, and DELETE requests:

GET /api/songs: Retrieves a list of all songs in the app's database.
GET /api/songs/{id}: Retrieves a specific song from the app's database, using its ID.
POST /api/songs: Adds a new song to the app's database.
PUT /api/songs/{id}: Updates a specific song in the app's database, using its ID.
DELETE /api/songs/{id}: Deletes a specific song from the app's database, using its ID.
GET /api/genres: Retrieves a list of all music genres in the app's database.
GET /api/genres/{id}: Retrieves a specific music genre from the app's database, using its ID.
POST /api/genres: Adds a new music genre to the app's database.
PUT /api/genres/{id}: Updates a specific music genre in the app's database, using its ID.
DELETE /api/genres/{id}: Deletes a specific music genre from the app's database, using its ID.

## Conclusion
The Tigerify app developed in Python and Angular is a powerful music streaming platform that offers a wide range of features and functionality. 

With support for a wide variety of music genres and a set of endpoints for GET, POST, PUT, and DELETE requests, the app provides a seamless and intuitive music streaming experience for users.

