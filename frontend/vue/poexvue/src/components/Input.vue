<template>
    <button @click="clearInputs">X</button>
    <input v-if="length == 0" v-model="account" type="text" placeholder="PoE Account">
    <input v-else v-model="account_name" type="text" disabled>
    <button v-if="length == 0" @click="fetchCharacters">Go</button>
</template>
<script>
export default {
    data() {
        return {
            account: ""
        }
    },
    props: ['length']
}
</script>
<style>
    
</style>