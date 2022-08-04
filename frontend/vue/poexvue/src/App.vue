<template>
    <div>
        <fetch-account></fetch-account>
        <get-snapshots></get-snapshots>
        <!-- <character-inventory/> -->
    </div>
</template>

<script>
import FetchAccount from "@/components/FetchAccount.vue"
import GetSnapshots from "@/components/GetSnapshots.vue"
import CharacterInventory from "@/components/CharacterInventory.vue"

export default {
    components: {
        FetchAccount,
        GetSnapshots,
        CharacterInventory,
    }
}
</script>

<style scoped>
    div {
        margin-top: 15px;
    }
</style>
