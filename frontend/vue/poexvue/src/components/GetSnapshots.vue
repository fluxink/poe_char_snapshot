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
    <div v-if="snapshots.length > 1">
        <apexchart @mounted="selectFirst" @dataPointSelection="selectSnapshot" ref="chart" width="500" type="bar" :options="chart_options" :series="chart_data"></apexchart>
        <div>
            <button @click="prevSnapshot">Previous</button>
            <span>{{snapshots[current_snapshot_number].time}}</span>
            <button @click="nextSnapshot">Next</button>
        </div>
    </div>
    <character-inventory v-if="snapshots.length >= 1" :items="snapshots[current_snapshot_number].items"/>

</template>
<script>
import VueApexCharts from "vue3-apexcharts"
import CharacterInventory from "@/components/CharacterInventory.vue"
import * as MyUtils from "@/modules/myutils.js"

export default {
    components: {
        apexchart: VueApexCharts,
        CharacterInventory
    },
    data(){
        return {
            account: "",
            characters: [],
            snapshots: [],
            selected_character: "",
            chart_data: [],
            chart_options: [],
            items: [],
            current_snapshot_number: 0
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
            this.snapshots = []
            this.current_snapshot_number = 0
        },
        async fetchCharacterSnapshots(e){
            let response = await fetch("http://127.0.0.1:8000/api/get/" + this.account + "/" + this.selected_character, {
                method: "GET"
            })
            let result = await response.json()
            console.log(result)

            let data = MyUtils.getTimeAndExp(result)
            this.chart_options = {
                xaxis: {
                    type: 'category',
                    categories: data[0],
                },
                yaxis: {
                    labels: {
                        formatter: MyUtils.numberWithCommas
                        }
                    },
                chart: {
                    toolbar: {
                        show: false
                    },
                },
                title: {
                    text: 'Snapshots',
                    align: 'center'
                }
            }

            this.chart_data = [{
                name: 'Expirience',
                data: data[1]
            }]
            this.snapshots = result
        },
        nextSnapshot(e){
            if (this.current_snapshot_number == this.snapshots.length - 1){
                this.current_snapshot_number = 0
            }
            else {
                this.current_snapshot_number++
            }
            this.$refs.chart.toggleDataPointSelection(0, this.current_snapshot_number)
        },
        prevSnapshot(){
            if (this.current_snapshot_number == 0){
                this.current_snapshot_number = this.snapshots.length - 1
            }
            else {
                this.current_snapshot_number--
            }
            this.$refs.chart.toggleDataPointSelection(0, this.current_snapshot_number)
        },
        selectFirst(event, chartContext, config){
            this.$refs.chart.toggleDataPointSelection(0, 0)
        },
        selectSnapshot(event, chartContext, config){
            this.current_snapshot_number = config.selectedDataPoints
        }
    },
}
</script>
<style scoped>
    .get-snapshots {
        border-width: 1px;
        border-style: solid;
    }
</style>