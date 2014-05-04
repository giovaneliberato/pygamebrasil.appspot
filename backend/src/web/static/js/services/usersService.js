app.factory('Users', function($resource){
    return $resource(
        "/rest_api/users/get_all_users/:Id",
        {Id: "@Id"},
        {
            'save': {method: "POST", url: "/rest_api/users/add_user/"},
            'delete': {method: "POST",  url: "/rest_api/users/remove_user/"}
        }
    );
});