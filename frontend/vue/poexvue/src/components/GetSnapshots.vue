<template>
    <div class="get-snapshots">
        <h3>Get Snapshots</h3>
        <button @click="clearAccount">X</button>
        <input v-if="characters.length == 0" v-model="account" type="text" placeholder="PoE Account">
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
    <div v-if="snapshots.length >= 1">
        <apexchart width="500" type="bar" :options="chart_options" :series="snapshots"></apexchart>
    </div>
    <character-inventory v-if="items.length > 1" :items="items"/>

</template>
<script>
import SnapshotChart from "@/components/SnapshotChart.vue"
import VueApexCharts from "vue3-apexcharts"
import CharacterInventory from "@/components/CharacterInventory.vue"
import "@/modules/processSnapshots.js"

export default {
    components: {
        SnapshotChart,
        apexchart: VueApexCharts,
        CharacterInventory
    },
    data(){
        return {
            account: "",
            characters: [],
            selected_character: "",
            snapshots: [],
            chart_options: [],
            items: []
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

            let labels = []
            let exp = []
            for (let snapshot of result){
                console.log(snapshot)
                labels.push(snapshot.time)
                exp.push(snapshot.character_info.experience)
            }

            this.chart_options = {
                xaxis: {
                    categories: labels
                }
            }
            this.snapshots = [{
                name: 'Expirience',
                data: exp
            }]
            this.items = result[0].items
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