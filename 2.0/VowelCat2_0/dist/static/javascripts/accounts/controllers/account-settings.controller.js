!function(){"use strict";function t(t,n,e,o,r){function u(){function u(t){i.account=t.data}function a(){t.url("/"),r.error("That user does not exist.")}var c=e.getAuthenticatedAccount(),s=n.username.substr(1);c?c.username!==s&&(t.url("/"),r.error("You are not authorized to view this page.")):(t.url("/"),r.error("You are not authorized to view this page.")),o.get(s).then(u,a)}function a(){function t(){e.unauthenticate(),window.location="/",r.show("Your account has been deleted.")}function n(t){r.error(t.error)}o.destroy(i.account.username).then(t,n)}function c(){function t(){r.show("Your account has been updated.")}function e(t){r.error(t.error)}var u=n.username.substr(1);o.update(u,i.account).then(t,e)}var i=this;i.destroy=a,i.update=c,u()}angular.module("thinkster.accounts.controllers").controller("AccountSettingsController",t),t.$inject=["$location","$routeParams","Authentication","Account","Snackbar"]}();