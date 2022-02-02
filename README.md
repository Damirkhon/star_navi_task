# star_navi_task

### Create Account - POST request 
```sh
/api/register/ 
with JSON :
{
    "username":"<username>",
    "password":"<password>",
    "email":"<email>"
} 
```
### Login to get tokens- POST request 
```sh
/api/login/
with JSON :
{
    "username":"<username>",
    "password":"<password>"
} 
```
### Refresh access token - POST request
```sh
/api/refresh/
with JSON :
{
    "refresh":"<refreshToken>"
} 
```
### Create Post - POST request
```sh
/api/createPost/
with JSON 
{
    "title":"<title>",
    "content":"<content>"
}
```
### Like Post - POST request
```sh
/api/likePost/<postID>/
```
### Unlike Post - POST request
```sh
/api/unlikePost/<postID>/
```
### Get analytics on likes aggregated by day - GET request
```sh
/api/analitics/?date_from=<dateFrom>&date_to=<dateTo>/
```
### Get user activity information: last login time, last request time - GET request
```sh
/api/lastLogin/
```
