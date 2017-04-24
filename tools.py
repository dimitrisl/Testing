
import logging
import os


def set_logger(filename= os.path.abspath(__file__)+'access.log'):
    """
    Function that instantiates
    :param filename:
    :return:
    """

    log_formatter = logging.Formatter("%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s")
    root_logger = logging.getLogger(__name__)
    root_logger.setLevel(logging.DEBUG)
    # setting file handler for logger
    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)

    return root_logger


def send_email(recipient, subject, text):
    import smtplib

    gmail_user = os.environ.get('mail_user') # ergasia.netsec@gmail.com
    gmail_pwd = os.environ.get('mail_pass') # ergasiaasfaleiasdiktuwn

    to_ = recipient if type(recipient) is list else [recipient]

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (gmail_user, ", ".join(to_), subject, text)
    try:
        # SMTP_SSL Example
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()  # optional, called by login()
        server_ssl.login(gmail_user, gmail_pwd)
        # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
        server_ssl.sendmail(gmail_user, to_, message)
        # server_ssl.quit()
        server_ssl.close()
        print 'successfully sent the mail'
        print 'successfully sent the mail'
    except Exception as e:
        logger.exception(e)
        print "failed to send mail"

logger = set_logger()
