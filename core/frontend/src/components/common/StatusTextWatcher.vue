<template>
  <v-textarea auto-grow :value="all_messages" readonly />
</template>

<script lang="ts">
import mavlink2rest from '@/libs/MAVLink2Rest'
import Listener from '@/libs/MAVLink2Rest/Listener'

export default {
  name: 'StatusTextWatcher',
  props: {
    filter: {
      type: RegExp,
      default: '',
    },
  },
  data() {
    return {
      messages: [] as string[],
      listener: undefined as undefined | Listener,
      filterRegex: /.*/,
    }
  },
  computed: {
    all_messages(): string {
      return this.messages.join('\n')
    },
  },
  watch: {
    filter(newFilter) {
      this.filterRegex = new RegExp(newFilter)
    },
  },
  mounted() {
    this.listener = mavlink2rest.startListening('STATUSTEXT').setCallback((receivedMessage) => {
      const text = receivedMessage.message.text.join('')
      if (this.messages?.[this.messages.length - 1] === text) {
        return
      }
      if (new RegExp(this.filter).test(text)) {
        this.$emit('message', text)
      }
      this.messages.push(text)
    })
  },
  beforeDestroy() {
    this.listener?.discard()
  },
}

</script>
