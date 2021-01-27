import Auth from './auth'

import './middleware'

// Active schemes
import scheme_003d9a64 from './schemes/local.js'
import scheme_23514a38 from './schemes/oauth2.js'

export default function (ctx, inject) {
  // Options
  const options = {"resetOnError":false,"scopeKey":"scope","rewriteRedirects":true,"fullPathRedirect":false,"watchLoggedIn":true,"redirect":false,"vuex":{"namespace":"auth"},"cookie":{"prefix":"auth.","options":{"path":"/","expires":7}},"localStorage":{"prefix":"auth."},"token":{"prefix":"_token."},"refresh_token":{"prefix":"_refresh_token."},"defaultStrategy":"local","fetchUserOnLogin":true}

  // Create a new Auth instance
  const $auth = new Auth(ctx, options)

  // Register strategies
  // local
  $auth.registerStrategy('local', new scheme_003d9a64($auth, {"endpoints":{"login":{"url":"/dj-rest-auth/login/","method":"post","propertyName":false},"logout":{"url":"/dj-rest-auth/logout/","method":"post"},"user":{"url":"/dj-rest-auth/user/","method":"get","propertyName":false}},"_name":"local"}))

  // social
  $auth.registerStrategy('social', new scheme_23514a38($auth, {"response_type":"code","client_id":"1fbb5875a4d54eacb428597945516e2b","client_secret":"80a0332f48ce47e5a2025c469601b9a2","authorization_endpoint":"https://oauth.yandex.ru/authorize?","userinfo_endpoint":"https://login.yandex.ru/info?","scope":["login:avatar","login:email","login:info","login:birthday"],"access_type":"offline","access_token_endpoint":"https://oauth.yandex.ru/token?","token_type":"Bearer","grant_type":"authorization_code","redirect_uri":"http://fishow.ru/","token_key":"access_token","force_confirm":"yes","state":"","_name":"social"}))

  // Inject it to nuxt context as $auth
  inject('auth', $auth)
  ctx.$auth = $auth

  // Initialize auth
  return $auth.init().catch(error => {
    if (process.client) {
      console.error('[ERROR] [AUTH]', error)
    }
  })
}
