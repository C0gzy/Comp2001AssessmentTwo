# Trail Micro-Service - By Thomas Cogzell

## Setup
>[!IMPORTANT]
>This program uses Docker and DockerImage to run please install Docker before attempting to run it


## How To Use
- connection point is at: (http://localhost:3000/api/ui).
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

- http://localhost:3000/api/users
- http://localhost:3000/api/users/1

### TrailPont
