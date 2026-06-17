import {defineStore} from "pinia";
import {ref} from "vue";


export const useUserStore = defineStore('user', () => {
    const id = ref('1')
    const username = ref('gyxgyxgyxgyxgyxgyxgyxgyxgyxxxxxxxxxxxxxxxxxxxxxxxx')
    const photo = ref('http://127.0.0.1:8000/media/user/photos/default.jpg')
    const profile = ref('11')
    const accessToken = ref('11')

    function isLogin() {
        return accessToken.value !== ''
    }

    function setAccessToken(token) {
        accessToken.value = token
    }

    function setUserInfo(data){
        id.value = data.id
        username.value = data.username
        photo.value = data.photo
        profile.value = data.profile
    }

    function logout(){
        id.value = 0
        username.value = ''
        photo.value = ''
        profile.value = ''
        accessToken.value = ''
    }

    return {
        id,
        username,
        photo,
        profile,
        accessToken,
        isLogin,
        setAccessToken,
        setUserInfo,
        logout
    }
})


