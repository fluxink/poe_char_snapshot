<template>
    <div class="fetch-account">
        <h3>Import Character</h3>
        <button @click="clearAccount">X</button>
        <input v-if="characters.length == 0" v-model="account_name" type="text" placeholder="PoE Account">
        <input v-else v-model="account_name" type="text" disabled>
        <button v-if="characters.length == 0" @click="fetchCharacters">Go</button>
        <select v-if="characters.length >= 1" v-model="selected_char">
            <option v-for="character in characters" :value="character">
                {{character.league}} {{ character.level }}, {{character.name}}, {{character.class}}
            </option>
        </select>
        <button v-if="selected_char != ''" @click="trackCharacter">Track</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            account_name: "",
            characters: [],
            selected_char: ""
        }
    },
    methods: {
        async fetchCharacters(e){
            let response = await fetch("http://127.0.0.1:8000/api/get-characters", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({account_name: this.account_name})
            })
            let result = await response.json()
            
            this.characters = JSON.parse(result)
        },
        clearAccount(e){
            this.account_name = ""
            this.characters = []
        },
        async trackCharacter(e){
            let request = await fetch("http://127.0.0.1:8000/api/edit/" + this.account_name, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    account: {
                        account_name: this.account_name,
                    },
                    character: this.selected_char.name,
                    league: this.selected_char.league,
                    tracked: true
                })
            })
        }
    }
}
</script>

<style scoped>
    .fetch-account {
        border-width: 1px;
        border-style: solid;
    }
</style>