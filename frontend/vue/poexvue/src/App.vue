<template>
    <div>
        <fetch-account></fetch-account>
        <get-snapshots></get-snapshots>
    </div>
</template>

<script>
import FetchAccount from "@/components/FetchAccount.vue"
import GetSnapshots from "@/components/GetSnapshots.vue"

export default {
    components: {
        FetchAccount,
        GetSnapshots
    }
}
</script>

<style scoped>
    div {
        margin-top: 15px;
    }
</style>
