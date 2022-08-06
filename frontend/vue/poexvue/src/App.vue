<template>
    <div>
        <fetch-account/>
        <get-snapshots v-model="snapshots"/>
        <snapshot-detail v-if="snapshots.length > 0" :snapshots="snapshots" :chart_data="chart_data" :chart_options="chart_options" />
        <!-- <character-inventory/> -->
    </div>
</template>

<script>
import FetchAccount from "@/components/FetchAccount.vue"
import GetSnapshots from "@/components/GetSnapshots.vue"
import CharacterInventory from "@/components/CharacterInventory.vue"
import SnapshotDetail from "./components/SnapshotDetail.vue"
import * as MyUtils from "@/modules/myutils.js"

export default {
    components: {
        FetchAccount,
        GetSnapshots,
        CharacterInventory,
        SnapshotDetail
    },
    data() {
        return {
            snapshots: [],
            chart_options: [],
            chart_data: []
        }
    },
    watch: {
        snapshots(value){
            let data = MyUtils.getTimeAndExp(this.snapshots)
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
        }
    }
}
</script>

<style scoped>
    div {
        margin-top: 15px;
    }
</style>
