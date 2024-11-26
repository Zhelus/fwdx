<template>
  <div class="form-container">
    <img id="fwdx-image" src="@/assets/bioblade.svg" />
    <form @submit.prevent="submitForgotPassword">
      <h2>Reset Password</h2>
      <p>Please enter your email address. You will receive a link to create a new password via email.</p>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div>
        <button type="submit" class="nav-button standard">Send Reset Link</button>
      </div>
      <div>
        <!-- Return to Login Page link -->
        <a @click="returnToLogin" class="return-link">Return to Login Page</a>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'ForgotPasswordView',
  data() {
    return {
      email: ''
    };
  },
  methods: {
    submitForgotPassword() {
      // Here you'd typically make an API call to your backend to handle the password reset request
      console.log("Reset link sent to:", this.email);
      alert("If the email is in our system, you will receive a password reset link.");
      // Optionally reset the input field or redirect the user
      this.email = '';
    },
    returnToLogin() {
      this.$router.push('/'); // Adjust the route as necessary
    }
  }
};
</script>

<style scoped>
.form-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  text-align: center;
}

#fwdx-image {
  width: 60%; /* Example: Resize width to 50% of its container */
  height: auto; /* Maintains the aspect ratio of the image */
  margin-bottom: 1.5rem;
  margin-top: 2rem;
}

.return-link {
  display: block;
  margin-top: 1rem;
  color: #0056b3; /* Example: use your theme blue color */
  background-color: transparent;
  border: none;
  text-decoration: underline;
  cursor: pointer;
  padding: 10px 15px;
}

.return-link:hover {
  background-color: #f4f4f4; /* Light grey background on hover */
}

input[type="email"] {
  width: 100%;
  padding: 10px;
  margin-top: 8px;
  margin-bottom: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: #000; /* Dark text for input */
}

button {
  color: white;
  background-color: var(--fwdx-blue);
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  width: 100%;
}

button:hover {
  background-color: var(--fwdx-blue-button-hover);
}

label, h2, p {
  color: #222; /* Darkened text color for better readability */
  font-size: 1rem;
}

h2 {
  margin-bottom: 0.8rem;
  font-size: 1.5rem; /* Adjusted size for better visibility */
}

p {
  font-size: 1rem;
  margin-bottom: 1rem; /* Proper spacing for introductory text */
}

button:hover {
  background-color: #ffc906;
}
</style>


