# Privacy and Compliance

## Overview
This document describes the datasets used in the social-analyzer project and provides recommendations for compliance with privacy regulations.

## Datasets

### Social Media Sites Database (data/sites.json)
- **Purpose**: Contains metadata about social media websites for profile detection
- **Content**: Website URLs, detection patterns, metadata for analysis
- **Privacy Impact**: Does not contain personal data; only public website information
- **Usage**: Used to construct search queries and validate profile existence

### Language Database (data/languages.json)
- **Purpose**: Language detection and internationalization support
- **Content**: Language codes, detection patterns
- **Privacy Impact**: No personal data
- **Usage**: Text analysis and language identification

### Dictionary Data (data/dict.json)
- **Purpose**: Common words and patterns for username analysis
- **Content**: Public dictionary words
- **Privacy Impact**: No personal data
- **Usage**: Username pattern matching

### Names Database (data/names.json)
- **Purpose**: Common names for analysis
- **Content**: Public name lists
- **Privacy Impact**: No personal data; common names only
- **Usage**: Name-based search patterns

### Countries Database (data/countries.json)
- **Purpose**: Geographic filtering capabilities
- **Content**: Country codes and metadata
- **Privacy Impact**: No personal data
- **Usage**: Geographic-based website filtering

### Thai Law Enforcement Data Files
**⚠️ IMPORTANT: These files contain sensitive law enforcement data.**

- `บัญชีหมายจับที่ยังไม่จับกุม บก.ปส.3.csv` (Arrest warrant list CSV)
- `บัญชีหมายจับที่ยังไม่จับกุม บก.ปส.3.xlsx` (Arrest warrant list Excel)
- `ประกาศรายชื่อเป้าหมายสืบจับ ยาเสพติด ปี 2566 - สำเนา (2).pdf` (Drug enforcement targets PDF)

**Content**: Law enforcement data including names, IDs, and case information
**Privacy Impact**: HIGH - Contains personally identifiable information (PII)
**Legal Basis**: Owner confirmed data is allowed for research purposes
**Restrictions**: 
- DO NOT modify or delete these files
- Reference only, do not redistribute
- For research and analysis purposes only
- Must comply with local laws regarding law enforcement data

## Privacy Principles

### หลักการพื้นฐาน (Fundamental Principles)
- **Minimization**: เก็บเฉพาะข้อมูลที่จำเป็น (Collect only necessary data)
- **Pseudonymization**: แยก PII ออกจาก metadata เชิงวิเคราะห์ (Separate PII from analytical metadata)
- **Segregation of Duties**: การเข้าถึงภาพ/ไฟล์จริงต้องผ่าน workflow ที่มีผู้อนุมัติ (Access to actual images/files requires approved workflow)
- **Audit & Chain-of-Custody**: บันทึกทุกการเข้าถึง และเหตุผลในการเข้าถึง (Log all access and reasons)

## Recommendations for Compliance

### For Research Use
1. **Data Minimization**: Only process data necessary for your research objectives
2. **Access Control**: Implement proper authentication and authorization
3. **Audit Logging**: Log all access to sensitive data files
4. **Retention Policy**: Define and enforce data retention periods
5. **Anonymization**: When possible, anonymize or pseudonymize data before analysis

### Legal Compliance (Thailand Context)
1. **PDPA Compliance**: Ensure compliance with Thailand's Personal Data Protection Act (PDPA)
2. **Law Enforcement Data**: Special handling required for law enforcement datasets
3. **Research Ethics**: Follow institutional review board (IRB) guidelines if applicable
4. **Data Transfer**: Be aware of cross-border data transfer restrictions

### Technical Safeguards
1. **Encryption**: Encrypt sensitive data at rest and in transit
2. **Access Logs**: Maintain detailed access logs with timestamps and user information
3. **Secure Storage**: Store sensitive files in secure, access-controlled locations
4. **Network Isolation**: Consider network segmentation for systems processing sensitive data

### การใช้ LPR (License Plate Recognition)
- ให้ใช้เฉพาะเมื่อมีอำนาจทางกฎหมายและมีนโยบายชัดเจน (Use only when legally authorized with clear policies)
- การจับคู่ป้ายทะเบียนควรผ่าน validation ของเจ้าหน้าที่ (License plate matching should undergo manual review)
- เก็บ logs ทุกครั้งที่มีการอ่าน/ค้นป้ายทะเบียน (Log every license plate read/search)

### การเก็บรักษา (Data Retention)
- กำหนด retention ตามกฎหมาย / นโยบายภายใน (Define retention according to law/internal policy)
- ลบข้อมูลอัตโนมัติเมื่อครบกำหนด (Automatically delete data when retention period expires)

## Disclaimer
The owner has confirmed that the included law enforcement data files are allowed for research purposes. However, users of this software are responsible for ensuring their use complies with all applicable laws and regulations in their jurisdiction. This software does not provide legal advice.

## Contact
For questions about data usage, privacy, or compliance, please contact the repository owner or your legal/compliance team.
