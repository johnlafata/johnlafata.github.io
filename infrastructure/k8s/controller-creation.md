
# build a controller
reference: https://www.youtube.com/watch?v=rDneUL1Cn_Q 

## define CRD format
* name it - define singular - plural
* define spec in openapiv3

## build client using language of your choice
https://github.com/kubernetes-client

## implement the client

### ensure there is an informer available for the watch function
- cache of objects so you don't need to keep polling database

### ensure the reconciler with the business logic to implement the desired state logic

### register our informer and run controller
