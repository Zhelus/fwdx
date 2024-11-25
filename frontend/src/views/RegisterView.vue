<template>
  <div class="form-container">
    <img id="fwdx-image" src="@/assets/bioblade.svg"  alt="DNA Sequence image"/>
    <form @submit.prevent="submitRegistration">
      <h2>Register</h2>
      <p>Please fill in this form to create an account.</p>
      <div>
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" v-model="firstName" required placeholder="Enter your first name">
      </div>
      <div>
        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" v-model="lastName" required placeholder="Enter your last name">
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required placeholder="Enter your email">
      </div>
      <div>
        <label for="phone_number">Phone Number:</label>
        <input type="phone_number" id="phone_number" v-model="phone_number" required placeholder="Enter your phone number">
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required placeholder="Enter your password">
      </div>
      <div>
        <label for="confirmPassword">Confirm Password:</label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required placeholder="Confirm your password">
      </div>
      <div>
        <button type="submit" class="nav-button standard">Register</button>
      </div>
      <div>
        <!-- Return to Login Page link -->
        <a @click="returnToLogin" class="return-link">Return to Login Page</a>
      </div>
    </form>
  </div>
</template>

<script>
import usersApiHelper from "@/services/usersApiHelper.js";

export default {
  name: 'RegisterView',
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      phone_number: '',
      password: '',
      confirmPassword: ''
    };
  },
  methods: {
    submitRegistration() {
      if (this.password !== this.confirmPassword) {
        alert("Passwords do not match.");
        return;
      }
      usersApiHelper.registerUser()
          .then(data => {
            console.log(data.status)
            if (data.status === 'success') {
              console.log("Registration attempted with:", this.firstName, this.lastName, this.email, this.phone_number, this.password);
              alert("Registration successful, please check your email to verify your account after admin approval.");
              // Optionally clear the form or redirect the user
              this.firstName = '';
              this.lastName = '';
              this.email = '';
              this.phone_number = '';
              this.password = '';
              this.confirmPassword = '';
              this.$router.push('/');

            } else {
              alert(data.message);
            }
          })
          .catch(error => {
            if (error.response) {
              // The request was made and the server responded with a status code
              // that falls out of the range of 2xx
              console.error('Error:', error.response.data);
              alert(error.response.data.message || 'Registration failed, please try again.');
            } else if (error.request) {
              // The request was made but no response was received
              console.error('Error:', error.request);
              alert('No response from server. Check your network connection.');
            } else {
              // Something happened in setting up the request that triggered an Error
              console.error('Error:', error.message);
              alert('Registration failed, please try again.');
            }
          });
    },
    returnToLogin(path) {
      this.$router.push(path)
    }
  }
};
</script>

<style scoped>
:root {
  --fwdx-blue: #0056b3; /* Primary blue color */
  --fwdx-hover-blue: #003975; /* Darker blue for hover states */
  --fwdx-text: #333; /* Default text color */
  --fwdx-background: #f4f4f4; /* Light background color */
  --fwdx-button-hover: #ffc906; /* Bright yellow for button hover, FWDX yellow */
}

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
  margin-bottom: 1.2rem;
  margin-top: 2rem;
}

.return-link {
  display: block;
  margin-top: 1rem;
  color: var(--fwdx-blue); /* Matching the primary blue color */
  background-color: transparent;
  text-decoration: underline;
  cursor: pointer;
  padding: 10px 15px;
}

.return-link:hover {
  background-color: #f4f4f4; /* Light grey background on hover */
}

input[type="email"],
input[type="phone_number"],
input[type="password"],
input[type="text"] {
  width: 100%;
  padding: 10px;
  margin-top: 8px;
  margin-bottom: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: #333; /* Ensuring inputs are also dark for consistency */
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
  color: #222; /* Slightly darker than #333 for more emphasis */
  font-size: 1rem;
}

h2 {
  margin-bottom: 0.5rem;
  font-size: 1.5rem; /* Slightly larger for heading emphasis */
}

p {
  font-size: 0.9rem; /* Slightly smaller for supplementary text */
  margin-bottom: 1rem; /* Spacing before form fields start */
}

button:hover {
  background-color: #ffc906;
}
</style>

