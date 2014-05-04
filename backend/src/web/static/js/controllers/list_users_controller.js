app.controller('listUsersController', function($scope, $window, Users){
    $scope.users = [];

    $scope.getAllUsers = function(){
        $scope.users = Users.query();
    };

    $window.onload = function(){
        $scope.getAllUsers();
    };

    $scope.removeUser = function(user, $index){
      $scope.users.splice($index, 1);
      Users.delete({}, {email: user.email});
    };

    $scope.addUser = function(){
        $scope.users.push( {'nome': $scope.name, 'email': $scope.email, 'google_id': $scope.id} );
        Users.save({}, {nome: $scope.name, email: $scope.email, id: $scope.id} );
    };
});
