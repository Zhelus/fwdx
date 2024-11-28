<script setup>
import { ref } from 'vue';

// Props
const props = defineProps({
  sectionHeader: String,
  modelValue: {
    type: Boolean,
    default: false, // Default to `false` if not provided
  },
});
const emit = defineEmits(['update:modelValue']); // Emit event for v-model binding

// Watch for changes and emit updates to the parent
function onCheckboxChange(event) {
  emit('update:modelValue', event.target.checked);
}
</script>

<template>
  <div class="checkbox-item-container">
    <h3 class="section-header">{{ sectionHeader }}</h3>
    <div class="checkbox-wrapper">
      <input
        class="form-checkbox"
        type="checkbox"
        :checked="modelValue"
        @change="onCheckboxChange"
        id="single-checkbox"
      />
      <label class="checkbox-label" for="single-checkbox">DNA Strand Positive?</label>
    </div>
  </div>
</template>

<style scoped>
.checkbox-item-container {
  display: flex;
  flex-direction: column;
  background-color: transparent;
  margin-bottom: 1rem;
}

.section-header {
  color: var(--dark-gray-text);
  font-size: var(--subheading-size);
  font-weight: var(--subheading-weight);
  margin-bottom: 0.5rem;
}

.checkbox-wrapper {
  display: flex;
  align-items: center;
}

.form-checkbox {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  height: 20px;
  width: 20px;
  border: 1px solid var(--light-gray-outline);
  border-radius: 2px;
  background-color: var(--fwdx-white);
}

.form-checkbox:checked {
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  appearance: checkbox;
  accent-color: var(--fwdx-yellow);
}

.checkbox-label {
  margin-left: 0.5rem;
  color: var(--dark-gray-text);
  font-size: var(--body-text-size);
}
</style>
