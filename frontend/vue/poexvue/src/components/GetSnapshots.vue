<template>
    <div class="get-snapshots">
        <h3>Get Snapshots</h3>
        <button @click="clearAccount">X</button>
        <input v-if="characters.length == 0" type="text" placeholder="PoE Account" v-model="account">
        <input v-else v-model="account" type="text" disabled>
        <button v-if="characters.length == 0" @click="fetchSavedCharacters">Get saved characters</button>
        <select v-if="characters.length >= 1" v-model="selected_character">
            <option disabled value="">Select Character</option>
            <option v-for="character in characters" :value="character.character">
                {{character.character}}
            </option>
        </select>
        <button v-if="characters.length >= 1" @click="fetchCharacterSnapshots">Retrive</button>
    </div>
</template>
<script>
export default {
    data(){
        return {
            account: "",
            characters: [],
            selected_character: ""
        }
    },
    methods: {
        async fetchSavedCharacters(e){
            let response = await fetch("http://127.0.0.1:8000/api/get/" + this.account, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                },
            })
            let result = await response.json()
            this.characters = result
        },
        clearAccount(e){
            this.account = ""
            this.characters = []
        },
        async fetchCharacterSnapshots(e){
            let response = await fetch("http://127.0.0.1:8000/api/get/" + this.account + "/" + this.selected_character, {
                method: "GET"
            })
            let result = await response.json()
            console.log(result)
        }
    }
}
</script>
<style scoped>
    .get-snapshots {
        border-width: 1px;
        border-style: solid;
    }
</style>