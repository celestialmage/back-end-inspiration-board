# Inspiration Board API Guide

The Inspiration Board API is separated into two areas, the `Board` endpoints, and the `Card` endpoints.

## `/boards` Endpoints

The `/boards` endpoints are focused around the manipulation of `boards` data, as well as a few endpoints that involve data related to boards, such as creating new cards from boards, and reading cards related to a specific board.

To achieve this, the `/boards` path has 5 endpoints:
- Creating new boards (POST `/boards`)
- Creating new cards for a board (POST `/boards/<board_id>/cards`)
- Getting all existing boards (GET `/boards`)
- Getting a single specific board (GET `/boards/<board_id>`)
- Getting all cards for a specific board (GET `/boards/<board_id>/cards`)

### POST `/boards`

This endpoint's functionality lies in creating a new board. When a `POST` reqiest is sent to this endpoint with the correct corresponding data, a new board will be created.

If the request is made with incorrect or missing `board` data, an error will be returned.

The new `board` to be created must look like the following.

```
{
    'title': 'Board's Title',
    'owner': 'James Cameron'
}
```

If the request is correctly formatted and a new `board` is created, a status code of `201` will be returned.

### POST `/boards/<board_id>/cards`

This endpoint's functionality lies in creating new cards. When a `POST` request is sent to this endpoint with the correct corresponding data, a new card will be created and associated with an existing `board`.

If a request is made with incorrect `card` data, or the associated `board` does not exist, an error will be returned. 

The given `card` data must be formatted like the following.

```
{
    'message': 'This is a card message!'
}
```

The `message` must be 40 characters or less in length. If the `message` is longer than 40 characters, an error will be returned.

On a success, a status message `201` will be returned.

### GET `/boards`

This endpoint's functionality lies in reading all existing `boards`.

When this endpoint is accessed a list of all `boards` is compiled and sent back to the requester. 

Optionally, the request can include OPTIONAL query parameter `sort` in order to sort the `boards` list in 3 different ways. An example would look like `/boards?sort=asc`.

When using the `sort` query parameter, you may use two different values to sort the returned `boards` by their `title` attribute. If you wish to sort in ascending order, you can set the `sort` query parameter to `"asc"`, and if you wish to sort them in descending order, give `sort` the `"desc"` value.

If the `sort` query parameter is not used, or if an invalid value is given to `sort`, the API will simply return a list of `boards` sorted by their `id`.

### GET `/<board_id>`

This endpoint's functionality is to return the information for a single board given that board's `board_id`.

If a board with the given `board_id` does not exist, an error code with status `404` will be returned.

On a success, a single board will be returned with status `200`.

### GET `/<board_id>/cards`

This endpoint's functionality lies in reading all cards for the given `board_id`.

When a `GET` request is made to this endpoint, the API will retrieve all cards that are associated with the given `board_id`. If a board with the given `board_id` is not found, an error with the status code `404` will be returned.

If successful, a list of cards will be returned with status `200`.

## `/cards` Endpoints

The `/cards` endpoints are focused on manipulation card data. There are two main endpoints to achieve this:
- Deleting existing `cards`
- Updating the `likes_count` attribute of a given `card`

Guides to these functionalities are shown below!

### DELETE `/cards/<card_id>`

This endpoint's functionality lies in removing a given card from the database.

If `card_id` is missing or points to a non-existant `card`, an error will be returned. 

On a success, a status message `204` will be returned.

### PATCH `/cards/<card_id>/like`

This endpoint's functionality lies in increasing the value of `likes_count` of the given `card`.

When this request is made, the API will verify that the given card exists. If it does, the API will access the card and increment its `likes_count` attribute by 1.

If `card_id` is missing or points to a non-existing card, an error will be returned.

On a success, a status message `204` will be returned.