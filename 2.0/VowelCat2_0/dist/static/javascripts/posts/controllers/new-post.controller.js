!function(){"use strict";function t(t,o,e,n,r){function c(){function c(){n.show("Success! Post created.")}function a(o){t.$broadcast("post.created.error"),n.error(o.error)}t.$broadcast("post.created",{content:s.content,author:{username:e.getAuthenticatedAccount().username}}),o.closeThisDialog(),r.create(s.content).then(c,a)}var s=this;s.submit=c}angular.module("thinkster.posts.controllers").controller("NewPostController",t),t.$inject=["$rootScope","$scope","Authentication","Snackbar","Posts"]}();