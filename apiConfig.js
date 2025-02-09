const API_CONFIG = {
  emailService: {
    provider: "emailjs",
    serviceId: "seu_service_id",
    templateId: "seu_template_id",
    userId: "seu_user_id",
  },
  backend: {
    url: "https://api.seuprojeto.com", // Aqui entraria a API futura
    endpoints: {
      sendEmail: "/send-email",
    },
  },
}

export default API_CONFIG
