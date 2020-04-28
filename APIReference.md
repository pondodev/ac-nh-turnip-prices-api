# api reference

## /api/Login (POST)

### body

```json
{
  username : "string"
}
```

### description

authenticates user. only uses a username for now because i don't want to handle proper authentication unless this application ends up getting bigger.

## /api/AllUsers (GET)

### description

returns an array in json format of all users.

## /api/User (GET)

### parameters

- id: string -- the user's id

### description

returns user with given id

## /api/User (POST)

### body

```json
{
    username: "string"
}
```

### description

creates new user in database. see [/api/Login](#/api/Login-(POST)) for why we only use usernames

## /api/UserPatterns (GET)

### parameters

- userId: int -- the user's id

### description

returns array of patterns owned by the user

## /api/SubmitPattern (PUT)

### body

```json
{
    userId  : 1,
    pattern : {
        startDate : 1587945600,
        prices    : "100.121.113..........",
        first     : False,
        pattern   : 0
    }
}
```

### description

places new pattern entry into database if it does not already exist, otherwise updates existing entry