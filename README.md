# Trail Micro-Service - By Thomas Cogzell

## Setup
>[!IMPORTANT]
>This program uses Docker and DockerImage to run please install Docker before attempting to run it

docker image can be found here (https://hub.docker.com/repository/docker/tomcogzell/comp2001/general) or at tomcogzell/comp2001:tagname

## To run docker image
```
    docker run -p 8000:8000 tomcogzell/comp2001:tagname
```
## How To Use
- connection point is at: (http://localhost:8000/api/ui).
- Connect to University network to access SQL database

>[!TIP]
>Data from the Api varies depending on wether a user is authenticated or not
>If you want the full data please login credentials in the header example below

### Header Layout
```
{
    "Email" : "string",
    "Password" : "string"
}
```

Accepted Auth Logins
```
{
    "Email" : "grace@plymouth.ac.uk",
    "Password" : "ISAD123!"
}
```

## API Endpoints
### Trail

### 1. Get All Trails
- **URL**: `/api/trails`
- **Method**: `GET`
- **Parameters** : `Login Credentials` in Header
- **Description**: Retrieve a list of all Trails.
- **Response**:
  - **200 OK**: Returns a JSON array of Trail objects.
  - **Example Response With Auth**:
    ```json
    [
      {
        "TrailDescription": "This is a gentle circular walk through ancient oak woodlands, beside the beautiful River Plym.",
        "TrailElevationgain": 147,
        "TrailImageFileLocation": "C:\\\\Images\\Plymbridge.png",
        "TrailLength": 5,
        "TrailName": "Plymbridge Circular",
        "TrailOwnerId": 1,
        "TrailRouteType": "Loop",
        "TrailStartingPointid": 1,
        "Trailid": 1,
        "USERS": 1
      },
    ]
    ```
  - **Example Response Without Auth**:
    ```json
    [
      {
        "TrailDescription": "This is a gentle circular walk through ancient oak woodlands, beside the beautiful River Plym.",
        "TrailElevationgain": 147,
        "TrailLength": 5,
        "TrailName": "Plymbridge Circular",
        "TrailRouteType": "Loop",
        "TrailStartingPointid": 1,
        "Trailid": 1
      },
    ]
    ```

### 2. Get Trail By ID
- **URL**: `/api/trails`
- **Method**: `GET`
- **Parameters** :
    - `Login Credentials` in Header
    - `id`
- **Description**: Retrieve a Trail.
- **Response**:
  - **200 OK**: Returns a JSON array of a Trail object.
  - **Example Response With Auth**:
    ```json
    [
      {
        "TrailDescription": "This is a gentle circular walk through ancient oak woodlands, beside the beautiful River Plym.",
        "TrailElevationgain": 147,
        "TrailImageFileLocation": "C:\\\\Images\\Plymbridge.png",
        "TrailLength": 5,
        "TrailName": "Plymbridge Circular",
        "TrailOwnerId": 1,
        "TrailRouteType": "Loop",
        "TrailStartingPointid": 1,
        "Trailid": 1,
        "USERS": 1
      },
    ]
    ```
  - **Example Response Without Auth**:
    ```json
    [
      {
        "TrailDescription": "This is a gentle circular walk through ancient oak woodlands, beside the beautiful River Plym.",
        "TrailElevationgain": 147,
        "TrailLength": 5,
        "TrailName": "Plymbridge Circular",
        "TrailRouteType": "Loop",
        "TrailStartingPointid": 1,
        "Trailid": 1
      },
    ]
    ```

### 3. Create a Trail
- **URL**: `api/trails/`
- **Method**: `POST`
- **Parameters** :
    - `Login Credentials` in Header
- **Description**: Add a new Trail to the SQL database
- **Request Body** (JSON):
   *   `"TrailName": "string",` string REQUIRED
   *   `"TrailOwnerId": 0,` int REQUIRED
   *   `"TrailElevationgain": 0,` int REQUIRED
   *   `"TrailImageFileLocation":` "string", string REQUIRED
   *   `"TrailLength": 0,` int REQUIRED
   *   `"TrailRouteType": "string",` string REQUIRED
   *   `"TrailDescription": "string",` string REQUIRED
   *   `"TrailStartingPointid": 0` int REQUIRED


- **Response**:
  - **201 Created**: Returns a success message upon creation.
  - **Example Response**:
    ```json
    {
      "Trailid": "1"
    }
    ```

### 4. Update a Trail
- **URL**: `api/trails/`
- **Method**: `POST`
- **Parameters** :
    - `Login Credentials` in Header
    - `id`
- **Description**: Add a new Trail to the SQL database
- **Request Body** (JSON):
   *   `"TrailName": "string",` string REQUIRED
   *   `"TrailOwnerId": 0,` int REQUIRED
   *   `"TrailElevationgain": 0,` int REQUIRED
   *   `"TrailImageFileLocation":` "string", string REQUIRED
   *   `"TrailLength": 0,` int REQUIRED
   *   `"TrailRouteType": "string",` string REQUIRED
   *   `"TrailDescription": "string",` string REQUIRED
   *   `"TrailStartingPointid": 0` int REQUIRED

- **Response**:
  - **200**: Returns a success message upon update.
  - **Example Response**:
    ```json
    {
       "message" : "Trail 1 Successfully Updated"
    }
    ```

### 5. Delete
- **URL**: `/api/trails/`
- **Method**: `DELETE`
- **Description**: Delete an Trail by their ID.
- **Parameters**:
  - `id`: Integer. The ID of the Trail to delete.
- **Response**:
  - **200 OK**: Returns a success message upon deletion.
  - **404 Not Found**: Returns an error message if the Trail is not found.
  - **Sample Response**:
    ```json
    {
      "message": "Trail 1 Successfully delted"
    }
    ```
### User

### 1. Get All Users
- **URL**: `/api/users`
- **Method**: `GET`
- **Parameters**: `Login Credentials` in Header (optional)
- **Description**: Retrieve a list of all Users.
- **Response**:
  - **200 OK**: Returns a JSON array of User objects.
  - **Authrised Example Response**:
    ```json
    [
      {
        "Userid": 1,
        "username": "john_doe",
        "Email": "john@example.com",
        "UserPermissionLevel": 1
      },
      ...
    ]
    ```
  - **UnAuthrised Example Response**:
    ```json
    [
      {
        "username": "john_doe",
      },
      ...
    ]
    ```

### 2. Get User By ID
- **URL**: `/api/users/{userId}`
- **Method**: `GET`
- **Parameters**:
  - `Login Credentials` in Header (optional)
  - `userId`: Integer. The ID of the User to retrieve.
- **Description**: Retrieve a User by their ID.
- **Response**:
  - **200 OK**: Returns a JSON object of the User.
  - **Authrised Example Response**:
    ```json
    {
      "Userid": 1,
      "username": "john_doe",
      "Email": "john@example.com",
      "UserPermissionLevel": 1
    }
    ```
  - **unAuthrised Example Response**:
    ```json
    [
      {
        "Userid": 1,
        "username": "john_doe",
      },
      ...
    ]
    ```
  - **404 Not Found**: Returns an error message if the User is not found.

### 3. Create a User
- **URL**: `/api/users`
- **Method**: `POST`
- **Parameters**: `Login Credentials` in Header 
- **Description**: Add a new User to the SQL database.
- **Request Body** (JSON):
  ```json
  {
    "username": "string",
    "Email": "string",
    "Password": "string",
    "UserPermissionLevel": 0
  }
  ```
- **Response**:
  - **201 Created**: Returns a success message upon creation.
  - **Example Response**:
    ```json
    {
      "Userid": 1
    }
    ```
  - **406 Not Acceptable**: Returns an error message if the User already exists.
  - **500 Internal Server Error**: Returns an error message if there is a server error.

### 4. Delete a User
- **URL**: `/api/users/{userId}`
- **Method**: `DELETE`
- **Parameters**:
  - `Login Credentials` in Header 
  - `userId`: Integer. The ID of the User to delete.
- **Description**: Delete a User by their ID.
- **Response**:
  - **200 OK**: Returns a success message upon deletion.
  - **404 Not Found**: Returns an error message if the User is not found.
  - **Example Response**:
    ```json
    {
      "message": "User 1 Successfully deleted"
    }
    ```

### TrailPoint 

### 1. Get All TrailPoints
- **URL**: `/api/trailpoints`
- **Method**: `GET`
- **Description**: Retrieve a list of all TrailPoints.
- **Response**:
  - **200 OK**: Returns a JSON array of TrailPoint objects.
  - **Example Response**:
    ```json
    [
      {
        "TrailPointid": 1,
        "TrailPointLatitude": 50.3755,
        "TrailPointLongitude": -4.1427,
        "NextTrailPointid": 2
      },
      ...
    ]
    ```

### 2. Get TrailPoint By ID
- **URL**: `/api/trailpoints/{trailPointId}`
- **Method**: `GET`
- **Parameters**:
  - `trailPointId`: Integer. The ID of the TrailPoint to retrieve.
- **Description**: Retrieve a TrailPoint by its ID.
- **Response**:
  - **200 OK**: Returns a JSON object of the TrailPoint.
  - **Example Response**:
    ```json
    {
      "TrailPointid": 1,
      "TrailPointLatitude": 50.3755,
      "TrailPointLongitude": -4.1427,
      "NextTrailPointid": 2
    }
    ```
  - **404 Not Found**: Returns an error message if the TrailPoint is not found.

### 3. Create a TrailPoint
- **URL**: `/api/trailpoints`
- **Method**: `POST`
- **Parameters**: `Login Credentials` in Header 
- **Description**: Add a new TrailPoint to the SQL database.
- **Request Body** (JSON):
  ```json
  {
    "TrailPointid": 1,
    "TrailPointLatitude": 50.3755,
    "TrailPointLongitude": -4.1427,
    "NextTrailPointid": 2
  }
  ```
- **Response**:
  - **201 Created**: Returns a success message upon creation.
  - **Example Response**:
    ```json
    {
      "TrailPointid": 1
    }
    ```
  - **406 Not Acceptable**: Returns an error message if the TrailPoint already exists.
  - **500 Internal Server Error**: Returns an error message if there is a server error.

### 4. Update a TrailPoint
- **URL**: `/api/trailpoints/{trailPointId}`
- **Method**: `POST`
- **Parameters**:
  - `Login Credentials` in Header 
  - `trailPointId`: Integer. The ID of the TrailPoint to update.
- **Description**: Update an existing TrailPoint in the SQL database.
- **Request Body** (JSON):
  ```json
  {
    "TrailPointLatitude": 50.3755,
    "TrailPointLongitude": -4.1427,
    "NextTrailPointid": 2
  }
  ```
- **Response**:
  - **200 OK**: Returns a success message upon update.
  - **Example Response**:
    ```json
    {
        "message" : "TrailPoint 1 Updated"
    }
    ```
  - **404 Not Found**: Returns an error message if the TrailPoint is not found.

### 5. Delete a TrailPoint
- **URL**: `/api/trailpoints/{trailPointId}`
- **Method**: `DELETE`
- **Parameters**:
  - `Login Credentials` in Header
  - `trailPointId`: Integer. The ID of the TrailPoint to delete.
- **Description**: Delete a TrailPoint by its ID.
- **Response**:
  - **200 OK**: Returns a success message upon deletion.
  - **404 Not Found**: Returns an error message if the TrailPoint is not found.
  - **Example Response**:
    ```json
    {
      "message": "TrailPoint with id 1 has been deleted"
    }
    ```
