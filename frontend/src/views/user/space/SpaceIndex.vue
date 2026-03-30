<script setup>
import {useRoute} from "vue-router";

const route = useRoute()
</script>

<template>
个人空间:{{route.params.userid}}
</template>

<style scoped>

</style>