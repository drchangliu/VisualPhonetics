!function(){"use strict";function t(t,n){function e(){return t.authenticatedAccount?JSON.parse(t.authenticatedAccount):void 0}function c(){return!!t.authenticatedAccount}function i(t,e){function c(t){s.setAuthenticatedAccount(t.data),window.location="/"}function i(){console.error("Epic failure!")}return n.post("/api/v1/auth/login/",{email:t,password:e}).then(c,i)}function o(){function t(){s.unauthenticate(),window.location="/"}function e(){console.error("Epic failure!")}return n.post("/api/v1/auth/logout/").then(t,e)}function u(t,e,c){function i(){s.login(t,e)}function o(){console.error("Epic failure!")}return n.post("/api/v1/accounts/",{username:c,password:e,email:t}).then(i,o)}function a(n){t.authenticatedAccount=JSON.stringify(n)}function r(){delete t.authenticatedAccount}var s={getAuthenticatedAccount:e,isAuthenticated:c,login:i,logout:o,register:u,setAuthenticatedAccount:a,unauthenticate:r};return s}angular.module("thinkster.authentication.services").factory("Authentication",t),t.$inject=["$cookies","$http"]}();