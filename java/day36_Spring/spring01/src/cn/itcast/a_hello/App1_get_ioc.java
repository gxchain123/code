package cn.itcast.a_hello;

import org.junit.Test;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

public class App1_get_ioc {

	// 1. ͨ��������õ�IOC���������Ķ���
	public void testIOC() throws Exception {
		// ��������
		// User user = new User();
		
		// ���ڣ��Ѷ���Ĵ�������spring��IOC����
		Resource resource = new ClassPathResource("cn/itcast/a_hello/applicationContext.xml");
		// ������������(Bean�Ĺ���), IOC���� = ������ + applicationContext.xml
		BeanFactory factory = new XmlBeanFactory(resource);
		// �õ����������Ķ���
		User user = (User) factory.getBean("user");
		
		System.out.println(user.getId());
		
	}
	
	//2. �����㣩ֱ�ӵõ�IOC��������
	@Test
	public void testAc() throws Exception {
		// �õ�IOC��������
		ApplicationContext ac = new ClassPathXmlApplicationContext("cn/itcast/a_hello/applicationContext.xml");
		// �������л�ȡbean
		User user = (User) ac.getBean("user");
		
		System.out.println(user);
	}

	public static void main(String[] args) {
		new App1_get_ioc().testAc();
	}
}








