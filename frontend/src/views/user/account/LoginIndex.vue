<script setup>

import {ref} from "vue";
import api from "@/js/http/api.js";
import {useUserStore} from "@/stores/user.js";
import router from "@/router/index.js";

const username = ref('')
const password = ref('')
const errorMessage = ref('')

const user = useUserStore()

async function handleLogin() {
  errorMessage.value = ''

  if (!username.value.trim()) {
    errorMessage.value = '账号不能为空'
  }else if (!password.value.trim()) {
    errorMessage.value = '密码不能为空'
  } else {
    try {
      const res = await api.post('api/user/account/login/', {
        username: username.value,
        password: password.value
      })

      const data = res.data
      if (data.result === 'success') {
        user.setAccessToken(data.access)
        user.setUserInfo(data)

        await router.push({
          name: 'homepage-index'
        })
      } else {
        errorMessage.value = data.result
      }

    } catch (error) {
      console.log(error)
    }
  }
}
</script>

<template>
  <div class="flex justify-center mt-25">
      <form @submit.prevent="handleLogin" class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
        <label class="label">账号</label>
        <input type="text" class="input" placeholder="请输入账号" v-model="username"/>

        <label class="label">密码</label>
        <input type="password" class="input" placeholder="请输入密码" v-model="password"/>

        <p v-if="errorMessage" class="textarea-sm text-sm text-red-500 mt-2">{{ errorMessage }} </p>

        <button class="btn btn-neutral mt-4">登录</button>
         <div class="flex justify-end mt-2">
          <RouterLink :to="{name: 'user-account-register-index'}" class="btn btn-sm">注册</RouterLink>
        </div>

      </form>
  </div>
</template>

<style scoped>

</style>