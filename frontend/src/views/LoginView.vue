<template>
  <div class="login-page">
    <div class="illustration-section">
      <!-- Placeholder for image, replace with actual image URL -->
      <img src="/Users/ntull/IdeaProjects/fwdx/frontend/src/assets/DNA_Background_FWDX.jpg" alt="Login Illustration">
    </div>
    <div class="login-container">
      <img id="fwdx-image" src="@/assets/bioblade.svg" />
      <h2>Sign in</h2>
      <form @submit.prevent="submitLogin">
        <div class="input-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" placeholder="Enter your email" required>
        </div>
        <div class="input-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" placeholder="Enter your password" required>
        </div>
        <button type="submit">Sign in</button>
        <a href="#" @click="navigate('/forgot_password')">Forgot password?</a>
        <hr>
        <p>Don’t have an account? <a @click="navigate('/register')">Sign Up</a></p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    submitLogin() {
      fetch('/api/v1/users/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: this.email, password: this.password })
      })
          .then(response => response.json())
          .then(data => {
            if (data.status === 'success') {
              this.$router.push('/home');
            } else {
              alert(data.message);
            }
          })
          .catch(error => {
            console.error('Error:', error);
            alert('Login failed, please try again.');
          });
    },
    navigate(path) {
      this.$router.push(path);
    }
  }
};
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* Ensure full viewport height */
  background-color: var(--fwdx-background);
  --fwdx-button-hover: #FFC906FF;
}

#fwdx-image {
  width: 60%; /* Example: Resize width to 50% of its container */
  height: auto; /* Maintains the aspect ratio of the image */
  margin-bottom: 3rem;
  margin-top: 2rem;
}

.illustration-section, .login-container {
  width: 60%; /* Split the page evenly */
  height: 100%;
}

.login-container {
  width: 40%; /* Split the page evenly */
  height: 100%;
}

.illustration-section img {
  width: 100%; /* Ensure the image covers the full section */
  height: 100vh; /* Match the height of the login section */
  object-fit: cover; /* Ensure the image is nicely fitted */
}

.login-container {
  padding: 20px;
  background: #fffcfc;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  text-align: center;
  color: #000; /* All text in black */
  display: flex;
  flex-direction: column;
  align-items: center; /* Center align flex items vertically */
}

.input-group {
  display: flex; /* Align label and input side by side */
  align-items: center; /* Center align items vertically */
  justify-content: flex-start; /* Align items to the start */
  margin-bottom: 15px;

}

label {
  width: 40%; /* Fixed width for consistency */
  min-width: 120px; /* Minimum width to handle longer labels */
  text-align: right; /* Align text to the right for a neater look */
  margin-right: 15px; /* Space between label and input */
  white-space: nowrap; /* Prevents the label from breaking into multiple lines */
}

input[type="email"], input[type="password"] {
  flex-grow: 1; /* Allows input to fill available space */
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: #000; /* Text color for inputs */
}

button {
  width: 40%;
  padding: 12px 20px;
  margin-top: 10px;
  background-color: var(--fwdx-blue);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover, a:hover {
  background-color: var(--fwdx-button-hover);
}

h1 {
  margin-top: 5rem;
  margin-bottom: 3rem; /* Added more space below the main title */
  font-size: 2.5rem; /* Increase the size of the font */
  color: var(--fwdx-yellow); /* Set the color to fwdx yellow */
  font-weight: bold; /* Make the text bold */
}

h2 {
  margin-bottom: 2rem;
  font-weight: bold; /* Make the text bold */
  color: var(--fwdx-blue)
}

hr {
  margin-top: 2rem; /* Added space above the horizontal rule */
  margin-bottom: 2rem; /* Added space below the horizontal rule */
  color: black;
}
a, p, label { /* Ensuring all text elements are in black */
  color: #000;
  margin-left: 1rem;
}

</style>
