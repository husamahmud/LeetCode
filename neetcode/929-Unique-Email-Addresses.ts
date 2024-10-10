function numUniqueEmails(emails: string[]): number {
  const unique: Set<string> = new Set();

  for (let email of emails) {
    // split the email into local and domain
    let [local, domain] = email.split('@')

    // remove all dots from the local and remove what's next the +
    local = local.replaceAll('.', '').split('+')[0]

    // add the correct formatted email to the unique set
    unique.add(local + '@' + domain)
  }

  return unique.size
};