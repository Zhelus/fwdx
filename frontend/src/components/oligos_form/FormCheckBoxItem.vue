<script setup>
import { ref, watch } from 'vue';

const props = defineProps(['sectionHeader', 'optionsList', 'modelValue']); // Add modelValue for v-model support
const emit = defineEmits(['update:modelValue']); // Declare the event for v-model updates

const selectedOptions = ref([...props.modelValue]); // Initialize selected options with the provided modelValue

// Watch for changes in selectedOptions and emit updates
watch(selectedOptions, (newValue) => {
  emit('update:modelValue', newValue);
});
</script>

<template>
  <div class="checkbox-item-container">
    <h3 class="section-header">{{ sectionHeader }}</h3>
    <div class="checkboxes-container">
      <div v-for="(option, index) in optionsList" :key="index" class="checkbox-wrapper">
        <input
          class="form-checkbox"
          type="checkbox"
          :value="option.value"
          :name="option.name + index"
          v-model="selectedOptions"
        />
        <label class="checkbox-label" :for="option.name + index">{{ option.name }}</label>
      </div>
    </div>
  </div>
</template>

<style scoped>
.checkbox-item-container {
  display: flex;
  flex-direction: column;
  height: 10%;
  width: 40%;
  min-width: 380px;
  background-color: transparent;
  margin-bottom: 2.5rem;
  margin-top: 0rem;
}

.checkboxes-container {
  display: flex;
  flex-wrap: wrap;
  height: 100%;
}

.section-header {
  color: var(--dark-gray-text);
  font-size: 16pt;
  font-weight: 700;
  line-height: auto;
  text-align: left;
  text-justify: top;
  margin-bottom: 0.25rem;
}

.checkbox-wrapper {
  width: 33%;
  height: 22%;
  background-color: transparent;
  display: flex;
  justify-content: flex-start;
  align-items: flex-end;
  padding: 0;
}

.form-checkbox {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 1.5vh;
  width: 1.5vh;
  outline: 0;
  border: 1px solid var(--light-gray-outline);
  border-radius: 2px;
  background-color: var(--fwdx-white);
}

.form-checkbox:hover {
  cursor: pointer;
  border: 1px solid var(--fwdx-yellow);
}

.form-checkbox:checked {
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  appearance: checkbox;
  accent-color: var(--fwdx-yellow);
}

.checkbox-label {
  color: var(--dark-gray-text);
  margin-left: 0.25rem;
  font-size: 12pt;
  align-self: flex-end;
  line-height: 1em;
}
</style>
